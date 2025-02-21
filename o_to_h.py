from obsidian_to_hugo import ObsidianToHugo
import path_files as pf

def filter_file(file_contents: str, file_path: str) -> bool:
    if 'draft: true' in file_contents:
        print(file_path)
        return True
    else:
        return False


obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=pf.vault_path,
    hugo_content_dir=pf.dump_path,
    filters=[filter_file],
)

obsidian_to_hugo.run()
