let { PythonShell } = require("python-shell");
const path = require('path');
var options = {
    mode: 'text',
    // for some reason I have to use ../extraResources/backend/ in prod and './extraResources/backend/' in dev'
    scriptPath: path.join(__dirname, './extraResources/backend/'),
}
let pyshell = new PythonShell("main.py", options);
pyshell.on("message", function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
});
pyshell.on('stderr', function (stderr) {
    console.log(stderr);
});
// electron will kill the python process on exit
