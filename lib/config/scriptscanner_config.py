class config(object):

    #list in the format (import_path, class_name)
    #scripts = [('Qsim.scripts.experiments.tickle.tickle_experiment', 'ticklescan')
    scripts = [('common.lib.servers.script_scanner.example_experiment', 'example_experiment')
               ]

    allowed_concurrent = {
    }

    launch_history = 1000
