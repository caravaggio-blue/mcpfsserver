This is a continuation of an ongoing development session we are having.  The initial prompts are below.


# Initial Prompt
I want to create a local MCP (Model Context Protocol) server that allows an LLM to perform tasks on the local filesystem. The tasks should include:

1. Reading a file's contents
2. Writing content to a file
3. Appending to a file
4. Listing directory contents
5. Extracting a ZIP file to a given folder
6. Executing a local bash script (inline or file)
7. Returning stdout, stderr, and exit status of executed commands

Please list the full set of technical requirements for such a server, considering:
- APIs needed (routes, expected inputs/outputs)
- Security constraints
- Runtime environment (e.g., Linux)
- Programming language and frameworks suggestions
- Error handling strategies
- Any required authentication or sandboxing strategies

For the above local MCP server that reads/writes files and executes shell scripts, list the possible security risks and best-practice mitigations for each.

Assume it's running on a developer's local machine but may interact with a powerful LLM.

Be specific about:
- Code injection
- Path traversal
- File overwrite/damage
- Unsafe shell commands
- User access control

For the local MCP server that supports file read/write and bash execution, suggest a comprehensive testing strategy.

Include:
- Unit tests for each task (e.g., file writing, zip extraction)
- Integration tests simulating LLM tool invocation
- Safety tests to ensure paths and inputs are sanitized
- Mock responses for bash output (stdout, stderr, exit codes)

Treat this as a tutorial.  I am not familar with Python and Flask and I want to learn.  So all development will be done in small steps where we will develop in layers, building slowly upon an initial skeleton based on my feedback and question at each stage.  Also keep the README.md up to date as a diary of our work and decisions.  You can maintain the README.md, I will write the code based on your suggestions.  You will post code in the chat, you will not write any code to files (except README.md)

Read the project structure and files to see how far we have gotten.  We have succesffully tested the current functionality of server.py running in docker.
