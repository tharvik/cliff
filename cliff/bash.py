import argparse
import sys


class BashCompletionAction(argparse.Action):
    """Provide a custom action to print the bash completion instructions.
    """
    def __call__(self, parser, namespace, values, option_string=None):
        app = self.default
        stdout = app.stdout
        command_manager = app.command_manager
        # for c in command_manager:
        #     stdout.write('%s\n' % c[0])
        stdout.write('complete -W "')
        stdout.write(' '.join(c[0].partition(' ')[0] for c in command_manager))
        stdout.write('" %s\n' % app.NAME)
        sys.exit(0)
