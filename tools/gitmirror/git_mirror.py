#! /usr/bin/env python

import os
import gerritlib.gerrit
def run_command(cmd, status=False, env=None):
    env = env or {}
    cmd_list = shlex.split(str(cmd))
    newenv = os.environ
    newenv.update(env)
    log.debug("Executing command: %s" % " ".join(cmd_list))
    p = subprocess.Popen(cmd_list, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, env=newenv)
    (out, nothing) = p.communicate()
    log.info("Return code: %s" % p.returncode)
    log.info("Command said: %s" % out.strip())
    if status:
        return (p.returncode, out.strip())
    return out.strip()

def git_command(repo_dir, sub_cmd, env=None):
    env = env or {}
    git_dir = os.path.join(repo_dir, '.git')
    cmd = "git --git-dir=%s --work-tree=%s %s" % (git_dir, repo_dir, sub_cmd)
    status, _ = run_command(cmd, True, env)
    return status

GERRIT_HOST="review.openstack.org"
GERRIT_PORT=29418
GERRIT_USER="yunhong-jiang"
GERRIT_KEY=None

LOCAL_REP_TOP='/home/yjiang5/work/repo'

def get_proj_list():
    gerrit = gerritlib.gerrit.Gerrit(GERRIT_HOST,
                                     GERRIT_USER,
                                     GERRIT_PORT,
                                     GERRIT_KEY)
    project_list = gerrit.listProjects()

    return project_list

def main():
    projects = get_proj_list()
    for proj in projects:
        (orig, projname) = proj.split('/')        


if __name__ == "__main__":
    main()
