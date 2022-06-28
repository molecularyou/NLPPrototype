<script>
  export let name;
  let currentDoi = "";
  import Search from "./Search.svelte";
  import DarkMode from "svelte-dark-mode";

  let theme;

  $: switchTheme = theme === "dark" ? "light" : "dark";
  $: document.body.className = theme;

</script>

<main>
  <DarkMode bind:theme />

  <Search doi={currentDoi} />
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
    background: #121212;
    color: #f1f8ff;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
