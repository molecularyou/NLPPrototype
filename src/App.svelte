<script>
  import Search from "./Search.svelte";
  import DarkMode from "svelte-dark-mode";
  import List from "./List.svelte";
  import ListItem from "./ListItem.svelte";
  import CSV from "./CSV.svelte";
  let currentDoi = "";
  let currentSubmitType = "abstract";
  let currentIDType = "doi";
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
  function handleChangeSubmitType(value) {
    currentSubmitType = value;
  }
  function handleChangeIDType(value) {
    currentIDType = value;
  }
  async function handleClick() {
    disableSubmit = true;
    items = [];
    await fetch(`http://127.0.0.1:9090/${currentSubmitType}?${currentIDType}=${encodeURIComponent(currentDoi)}`, { method: "GET" })
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
  <Search onChangeDOI={handleChangeDOI} onChangeIDType={handleChangeIDType}  iDType={currentIDType} submitType={currentSubmitType} onChangeSubmitType={handleChangeSubmitType} onClick={handleClick} {disableSubmit} />
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
