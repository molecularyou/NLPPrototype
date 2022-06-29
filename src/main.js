import App from './App.svelte';
let { PythonShell } = require("python-shell");
let pyshell = new PythonShell("./hello.py", { mode: "text" });

// end the input stream and allow the process to exit
// pyshell.end(function (err, code, signal) {
// 	if (err) throw err;
// 	console.log("The exit code was: " + code);
// 	console.log("The exit signal was: " + signal);
// 	console.log("finished");
// });
const app = new App({
	target: document.body,
	props: {
		shell: pyshell
	}
});

export default app;