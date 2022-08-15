###################
### ENVIRONMENT ###
###################
import os
import sys

### LOAD GSLAB MAKE
ROOT = '..'
gslm_path = os.path.join(ROOT, 'lib', 'gslab_make')

sys.path.append(gslm_path)
import gslab_make as gs

### PULL PATHS FROM CONFIG
PATHS = {
    'root': ROOT,
    'config': os.path.join(ROOT, 'config.yaml')
}
PATHS = gs.update_internal_paths(PATHS)

### LOAD CONFIG USER 
PATHS = gs.update_external_paths(PATHS)
gs.update_executables(PATHS)

############
### MAKE ###
############

### START MAKE
gs.remove_dir(['input', 'external'])
gs.clear_dir(['output', 'log'])
gs.start_makelog(PATHS)

### MAKE LINKS TO INPUT AND EXTERNAL FILES
inputs = gs.copy_inputs(PATHS, ['input.txt'])
externals = gs.copy_externals(PATHS, ['external.txt'])
gs.write_source_logs(PATHS, inputs + externals)
gs.get_modified_sources(PATHS, inputs + externals)

### FILL TABLES
gs.tablefill(template = 'code/tables.lyx', 
             inputs   = 'input/regression.csv', 
             output   = 'output/tables_filled.lyx')

### RUN SCRIPTS
gs.run_lyx(PATHS, program = 'code/paper.lyx')
gs.run_lyx(PATHS, program = 'code/online_appendix.lyx')
gs.run_lyx(PATHS, program = 'code/slides.lyx')

### LOG OUTPUTS
gs.log_files_in_output(PATHS)

### CHECK FILE SIZES
gs.check_module_size(PATHS)

### END MAKE
gs.end_makelog(PATHS)