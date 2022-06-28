<script>
  export let doi;
  function handleClick() {
    console.log('clicked');
  }
</script>

<div id="flex-container">
  <input type="search" id="doi" name="doi" bind:value={doi} />
  <select name="type" id="type">
    <option value="abstract">Abstract</option>
    <option value="paper">Paper</option>
  </select>
  <button on:click={handleClick}> Submit </button>
</div>

<style>
  #flex-container {
    margin: 0 auto;
    flex-direction: row;
  }
  button {
    border-radius: 5px;
    box-shadow: 3px 3px 0px #3F3351;
    background-color: white;
  }

  button:hover {
    background-color: #E9A6A6;
  }

  button:active {
    box-shadow: 0px 0px 0px #666;
    transform: translate(3px, 3px);
    transition: transform 0.1s;
  }
</style>
