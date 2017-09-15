console.log('[CUSTOMIZATION] loading sublime custom.js');
require(
    [
        "codemirror/keymap/sublime",
        "notebook/js/cell",
        "base/js/namespace"
    ],
    function(sublime_keymap, cell, IPython) {
        cell.Cell.options_default.cm_config.lineNumbers = true;
        cell.Cell.options_default.cm_config.keyMap = 'sublime';

        // 不修改Ctrl+Enter
        cell.Cell.options_default.cm_config.extraKeys['Cmd-Enter'] = function(){console.log('cmd-enter')};
        cell.Cell.options_default.cm_config.extraKeys['Ctrl-Enter'] = function(){console.log('ctrl-enter')};
        cell.Cell.options_default.cm_config.extraKeys['Shift-Enter'] = function(){};

        // 用空格代替tab
        cell.Cell.options_default.cm_config.extraKeys['Tab'] = function(cm){cm.replaceSelection("    " , "end");}

        // 设置已存在cell的格式
        var cells = IPython.notebook.get_cells();
        for (var cl=0; cl<cells.length; cl++) {
            cells[cl].code_mirror.setOption('lineNumbers', true);
            cells[cl].code_mirror.setOption('keyMap', 'sublime');
            cells[cl].code_mirror.setOption('extraKeys',
                {
                    "Cmd-Enter": function(){},
                    "Ctrl-Enter": function(){},
                    "Tab": function(cm){cm.replaceSelection("    " , "end");}
                }
            );            
        }
    }
);