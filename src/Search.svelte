<script>
  export let doi;
  function handleClick() {
    console.log('clicked');
  }
</script>

<div id="flex-container">
  <input type="search" id="doi" name="doi" bind:value={doi} />
  <button on:click={handleClick}> Submit </button>
</div>

<style>
  #flex-container {
    margin: 0 auto;
    flex-direction: row;
  }
  button {
    border-radius: 5px;
    box-shadow: 3px 3px 0px grey;
    background-color: white;
  }

  button:hover {
    background-color: orange;
  }

  button:active {
    box-shadow: 0px 0px 0px #666;
    transform: translate(3px, 3px);
    transition: transform 0.1s;
  }
</style>
