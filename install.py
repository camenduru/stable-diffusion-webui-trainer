import os, launch
from modules import scripts

sd_scripts_repo_commit_hash = os.environ.get('SD_SCRIPTS_COMMIT_HASH', "f0ae7eea950b93b1550dc34a782da3bafda2a8c0")
sd_scripts_repo = os.environ.get('SD_SCRIPTS_REPO', "https://github.com/camenduru/sd-scripts")
launch.git_clone(sd_scripts_repo, os.path.join(scripts.basedir(), "stable-diffusion-webui-train", "sd-scripts"), "SD Scripts", sd_scripts_repo_commit_hash)