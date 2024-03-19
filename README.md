## cpipe (CLI File Uploader)
Cloud pipe

### Overview
cpipe is a command-line tool for uploading and downloading files from a remote server. It provides a convenient way to manage files through simple commands in the terminal.

### Features
- **User Authentication**: Users can create accounts and log in securely to access the upload and download functionalities.
- **Upload**: Easily upload files to the server using the `upload` command. Supports uploading single or multiple files.
- **Download**: Download files from the server using the `download` command. Option to specify the file to download.
- **File Information**: Get information about files stored on the server, including file size, hash, and upload time.
- **Publish and Index**: Publish files to make them accessible to other users. Index files with friendly names for easy identification.
- **Check for Updates**: Automatically check for updates to the cpipe tool to ensure you're using the latest version.
- **Existence Check**: Check if a file exists on the server based on its hash.

### Usage
1. **Installation**: Clone the repository and install the required dependencies.

2. **Setup**: Create an account using the `signup` command or log in with an existing account using the `login` command.

3. **Uploading Files**: Use the `upload` command followed by the file path to upload a file to the server.

4. **Downloading Files**: Use the `download` command followed by the file name to download a file from the server.

5. **File Information**: Use the `info`/`ls` command to get information about all files stored on the server. Use `info <file_name>` to get information about a specific file.

6. **Publishing Files**: Use the `publish`/`index` command followed by the file path to publish a file to the server. Specify a friendly name for easy identification.

7. **get**: Use the `get` command followed by the frindly name to download published files.

8. **Checking for Updates**: Use the `check-for-update`/`update` command to check for updates to the cpipe tool.

9. **Existence Check**: Use the `exsist` command followed by the file path to check if a file exists on the server.


### Tips
- Use the `-f` flag to force commands like uploading and publishing, allowing you to overwrite existing files if necessary.
- Use the `-i` flag to show more detailed information, such as file hashes and upload times.
- Double-check file names and paths when using commands to avoid errors.
- Regularly check for updates to ensure you have the latest features and improvements.

### Contributions
Contributions to cpipe are welcome! Feel free to fork the repository, make changes, and submit pull requests for new features, bug fixes, or enhancements.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

**Full Changelog**: https://github.com/mahditmx/Cpipe/commits/linux/deb
**server**: http://cliserver.pythonanywhere.com/
**NOTE** This is just a fun tool and not for regular using
