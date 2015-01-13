#! /usr/bin/env python
import shlex
import Queue
import logging as log
import os
import gerritlib.gerrit
import subprocess
import threading
import time

from gerritlib import gerrit

#log = logging.getLogger('git_mirror')
def run_command(cmd, status=False, env=None, cwd=None):
    env = env or {}
    cmd_list = shlex.split(str(cmd))
    newenv = os.environ
    newenv.update(env)
    #log.debug("Executing command: %s" % " ".join(cmd_list))
    print("Executing command: %s" % " ".join(cmd_list))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, env=newenv, shell=True, cwd=cwd)
    (out, nothing) = p.communicate()
    #log.info("Return code: %s" % p.returncode)
    print("Return code: %s" % p.returncode)
    #log.info("Command said: %s" % out.strip())
    print("Command said: %s" % out)
    print("Error said: %s" % nothing)
    if status:
        return (p.returncode, out.strip())
    return out.strip()

def git_command(repo_dir, sub_cmd, env=None):
    env = env or {}
    git_dir = os.path.join(repo_dir, '.git')
    cmd = "git --git-dir=%s --work-tree=%s %s" % (git_dir, repo_dir, sub_cmd)
    status, _ = run_command(cmd, True, env)
    return status

def clone_project(orig, name, branch=None):
    if not branch:
        branch = 'master'
    print "clone_project %s %s" % (orig, name)
    remote = "http://git.openstack.org/" + orig + "/" + name
    local = LOCAL_REP_TOP + orig + "/" + name + ".git"
    cmds = 'git clone %s %s' % (remote, local)
    status, _ = run_command(cmds, True)
    

GERRIT_HOST="review.openstack.org"
GERRIT_PORT=29418
GERRIT_USER="yunhong-jiang"
GERRIT_KEY=None

LOCAL_REP_TOP='/home/yjiang5/GITMIRROR/'

def get_proj_list(gerrit):
    project_list = gerrit.listProjects()

    return project_list

project_locks = {}
project_thread = {}
class UpdateThread(threading.Thread):
    def __init__(self, proj):
        threading.Thread.__init__(self)
        self.proj = proj

    def run(self):
        path = LOCAL_REP_TOP + self.proj + ".git" + "/"
        print "The update path is %s" % path
        if not os.path.exists(path):
            print "Path %s does not exist, clone now" % path
            (orig, projname) = self.proj.split('/')
            clone_project(orig, projname)
        else:
            cmds ="git pull"
            status, _ = run_command(cmds, status=True, cwd=path)

def setup(gerrit):
    projects = get_proj_list(gerrit)
    repos = []
    count = 0
    for proj in projects:
        count = count+1
        lock = project_locks.get(proj, None)
        if not lock:
            lock = threading.Lock()
            project_locks[proj] = lock
        (orig, projname) = proj.split('/')
        repos.append((orig, projname))
#        clone_project(orig, projname)
        update_project(proj)
        if not count % 5:
            time.sleep(5)
    return repos


def update_project(proj):
    thread = UpdateThread(proj)
    lock = project_locks.get(proj)
    if not lock:
        print "No locks for proj %s" % proj
        return
    with lock:
        thread.start()

def main():
    gerrit = gerritlib.gerrit.Gerrit(GERRIT_HOST,
                                     GERRIT_USER,
                                     GERRIT_PORT,
                                     GERRIT_KEY)
    setup(gerrit)
    print "Finished setup"
    gerrit.startWatching()
    event=gerrit.getEvent()
    while event:
        try:
            event=gerrit.event_queue.get(block=True, timeout=10)
        except Queue.Empty:
            continue

        
        if event.get("type") in ("comment-added"):
            print "Get new comments"
        elif event.get("type") in ("change-merged"):
        #if event.get("type") in ("change-merged", "comment-added"):
            changes = event.get("change")
            project = changes.get("project")
            (orig, projname) = project.split("/")
            print "to update project %s with change %s event %s" % (project, changes, event.get("type"))
            update_project(project)



if __name__ == "__main__":
    main()
