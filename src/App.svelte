<script>
  import Search from "./Search.svelte";
  import DarkMode from "svelte-dark-mode";
  import List from "./List.svelte";
  import ListItem from "./ListItem.svelte";
  import CSV from "./CSV.svelte";
  let currentDoi = "";
  let requestResponse = [];
  let items = [];
  let disableSubmit = false;
  $: items = requestResponse
    ? requestResponse.map((response) => ({
        response: response,
        component: ListItem,
        doi: response.doi,
        selected: {
          size: [],
          fluid: [],
          age: [],
          sex: [],
          omic: [],
          controlGroup: [],
          healthyControlGroup: [],
          analyte: [],
          umls: [],
        },
      }))
    : [];
  function handleChangeDOI(value) {
    currentDoi = value;
  }
  async function handleClick() {
    disableSubmit = true;
    items = [];
    await fetch(`http://127.0.0.1:8080/?doi=${currentDoi}`, { method: "GET" })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        requestResponse = data;
      })
      .catch(function (error) {
        console.log(error);
      });
    disableSubmit = false;
  }
  let theme;

  $: theme === "dark" ? "light" : "dark";
  $: document.body.className = theme;
</script>

<main>
  <DarkMode bind:theme />
  <Search onChangeDOI={handleChangeDOI} onClick={handleClick} {disableSubmit} />
  <CSV {items} />
  <List {items} />
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  :global(.dark) {
    background: #1f1d36;
    color: #f1f8ff;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
