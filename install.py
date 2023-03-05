import os, launch
from modules import scripts

sd_scripts_repo_commit_hash = os.environ.get('SD_SCRIPTS_COMMIT_HASH', "46aee85d2a88e279d9a0a286f579f5f3434a3c56")
sd_scripts_repo = os.environ.get('SD_SCRIPTS_REPO', "https://github.com/camenduru/sd-scripts")
sd_scripts_dir = os.path.join(scripts.basedir(), "extensions", "stable-diffusion-webui-trainer", "sd-scripts")
launch.git_clone(sd_scripts_repo, sd_scripts_dir, "SD Scripts", sd_scripts_repo_commit_hash)

launch.run_pip("install diffusers==0.13.1", "diffusers==0.13.1 requirements for trainer extension")
launch.run_pip("install transformers==4.26.1", "transformers==4.26.1 requirements for trainer extension")
launch.run_pip("install ftfy==6.1.1", "ftfy==6.1.1 requirements for trainer extension")
launch.run_pip("install accelerate==0.16.0", "accelerate==0.16.0 requirements for trainer extension")
launch.run_pip("install bitsandbytes==0.37.0", "bitsandbytes==0.37.0 requirements for trainer extension")
launch.run_pip("install safetensors==0.2.8", "safetensors==0.2.8 requirements for trainer extension")

launch.run_pip(f"install {sd_scripts_dir}", "kohya_ss library requirements for trainer extension")