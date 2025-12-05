import pypandoc
import os
import subprocess

# pypandoc.download_pandoc()

def convert_docx_to_md(docx_path):
    base = os.path.splitext(docx_path)[0]
    md_output = f"{base}.md"
    media_dir = f"{base}_media"

    pypandoc.convert_file(
        docx_path,
        # to="markdown",
        to="gfm",
        format="docx",
        outputfile=md_output,
        extra_args=[f"--extract-media={media_dir}"]
    )
    print(f"Converted: {docx_path} → {md_output}")
    return md_output, media_dir


def git_push(commit_msg="Auto update documentation"):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=False)
    subprocess.run(["git", "push"], check=True)
    print("Changes pushed to repo.")

if __name__ == "__main__":
    docx = "project.docx"   # your file
    md, media = convert_docx_to_md(docx)
    # git_push("Updated docs via Python automation")
