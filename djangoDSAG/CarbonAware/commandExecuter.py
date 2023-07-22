import subprocess as sub
import os

def execute(command, directory, workingDir):
    
    os.chdir(directory)
    
    p = sub.Popen(command, stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate()
    
    print("\n\nFrom cmdExec:\n")
    print(output)

    os.chdir(workingDir)

    return output, errors