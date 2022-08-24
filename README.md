## ✒️ Overview

This project is an attempt to use Spacy to extract key information from papers hosted within the PubMed database. 

#### 🧐 What packages does the project use?

**`electron`** enables you to create desktop applications with pure JavaScript by providing a runtime with rich native (operating system) APIs. You could see it as a variant of the Node.js runtime that is focused on desktop applications instead of web servers.

**`electron-builder`** is used as a complete solution to package and build a ready for distribution (supports Numerous target formats) Electron app with "auto update" support out of the box.

**`electron-serve`** is used for Static file serving for Electron apps.

**`svelte`** is a radical new approach to building user interfaces. Whereas traditional frameworks like React and Vue do the bulk of their work in the browser, Svelte shifts that work into a compile step that happens when you build your app. Instead of using techniques like virtual DOM diffing, Svelte writes code that surgically updates the DOM when the state of your app changes.

**`concurrently`** is used to run multiple commands concurrently.

**`wait-on`** is used as it can wait for sockets, and http(s) resources to become available.
<br />

## 🚀 Getting Started

**Note:** If you wish to use npm over yarn then modify `package.json` by replacing `yarn` with `npm` in `electron-dev` and `preelectron-pack` scripts.
But I strongly recommend using <em>yarn</em> as it is a better choice when compared to <em>npm</em>.

**prereqs:** Python 3.x (tested on 3.10), flask, spacy, biopython

```bash
# install python dependencies
$ pip install Flask
$ pip install biopython
$ pip install spacy
$ pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.0/en_ner_bionlp13cg_md-0.5.0.tar.gz
$ python -m spacy download en_core_web_trf

# if you do not have yarn and node install node at https://nodejs.org/en/download/ and yarn at https://classic.yarnpkg.com/lang/en/docs/install/

# Install electron dependencies
$ yarn # or npm install

# Run your app
$ yarn electron-dev # or npm run electron-dev

# Package Your App
$ yarn electron-pack # or npm run electron-pack
```

## Usage
Application defaults are to use a PMID and only perform analysis on an abstract. If this is sufficient enter the PMID in the ID box and click submit. If not, use the dropdowns to swap between PMID and DOI as well as abstract/paper. Once the analysis is done the results for each category will be surfaced. Clicking one of these results will highlight the text in the application and select it for exporting. Once all appropriate results have been clicked/selected click export to generate a csv file. Multiple IDs may be entered per query and must be separated with commas (ie 12857,123938).

<h3>📋 License: </h3>
Licensed under the <a href="https://github.com/soulehshaikh99/create-svelte-electron-app/blob/master/LICENSE">MIT License</a>.
