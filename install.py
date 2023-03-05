import launch

sd_scripts_repo_commit_hash = os.environ.get('SD_SCRIPTS_COMMIT_HASH', "f0ae7eea950b93b1550dc34a782da3bafda2a8c0")
sd_scripts_repo = os.environ.get('SD_SCRIPTS_REPO', "https://github.com/camenduru/sd-scripts")
git_clone(sd_scripts_repo, os.path.join(modules.scripts.basedir(), "sd-scripts"), "SD Scripts", sd_scripts_repo_commit_hash)