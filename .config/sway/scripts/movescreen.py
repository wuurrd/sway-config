import sys

import i3ipc

i3 = i3ipc.Connection()

outputs = i3.get_outputs()
outputs = [o for o in outputs if o.active]
workspaces = i3.get_workspaces()
currentfocus = [w for w in workspaces if w.focused][0].output
current = 0
for i, workspace in enumerate(outputs):
    print(workspace.name)
    if workspace.name == currentfocus:
        current = i
next_workspace = current + 1
if outputs[next_workspace % len(outputs)].name == "xroot-0":
    next_workspace += 1

cmd = "move workspace to output %s" % outputs[next_workspace % len(outputs)].name
i3.command(cmd)
