function openExplorer() {
    const { dialog } = require('electron').remote;
    const fs = require('fs');

    dialog.showOpenDialog({
        properties: ['openDirectory']
    }).then(result => {
        if (!result.canceled) {
            const folderPath = result.filePaths[0];
            document.getElementById('location').value = folderPath;
        }
    }).catch(err => {
        console.log(err);
    });
}