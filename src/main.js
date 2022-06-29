import App from './App.svelte';
let { PythonShell } = require("python-shell");
let pyshell = new PythonShell("./hello.py", { mode: "text" });
pyshell.on("message", function (message) {
	// received a message sent from the Python script (a simple "print" statement)
	console.log(message);
  });
const app = new App({
	target: document.body,
	props: {
		shell: pyshell
	}
});

export default app;