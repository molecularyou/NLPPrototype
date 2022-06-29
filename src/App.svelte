<script>
  export let shell;
  let currentDoi = "";
  import Search from "./Search.svelte";
  import DarkMode from "svelte-dark-mode";

  let theme;

  $: switchTheme = theme === "dark" ? "light" : "dark";
  $: document.body.className = theme;

</script>

<main>
  <DarkMode bind:theme />

  <Search doi={currentDoi} shell={shell}/>
  <p>
    Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
    how to build Svelte apps.
  </p>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  :global(.dark) {
    background: #1F1D36;
    color: #f1f8ff;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
