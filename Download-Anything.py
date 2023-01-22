import subprocess

# Prompt the user for the URL
# Make sure ur URL ends with complete file path for example https://website.com/file/image.png or zip, rar, mpr, mov, mp3, exe, py, etc any extension
url = input("Enter the URL:")

# Prompt the user for the output file name
outfile = input("Enter the name of the Output:")

# Use the subprocess module to run the wget command
subprocess.run(["wget", "-nc", "-c", "-O", outfile, url])
# The -nc option means "no-clobber" and it will not overwrite an existing file. The -c option is "continue" and it will continue a download that was previously interrupted. The -O option allows to specify the output file name and the url is the url of the file to download, it will save the downloaded file with the specified name.

# Confirm that the file has been saved
print("File saved successfully", outfile)
