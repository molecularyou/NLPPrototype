<script>
  export let onChangeDOI;
  export let onClick;
  export let disableSubmit;
</script>

<div id="flex-container">
  <input type="search" id="doi" name="doi" on:change={(e)=> onChangeDOI(e.target.value)} placeholder="DOI" />
  <select name="type" id="type">
    <option value="abstract">Abstract</option>
    <option value="paper">Paper</option>
  </select>
  <button on:click={onClick} disabled={disableSubmit}> Submit </button>
</div>

<style>
  #flex-container {
    margin: 0 auto;
    flex-direction: row;
  }
  button {
    border-radius: 5px;
    box-shadow: 3px 3px 0px #3f3351;
    background-color: white;
  }

  button:hover {
    background-color: #e9a6a6;
  }

  button:active {
    box-shadow: 0px 0px 0px #666;
    transform: translate(3px, 3px);
    transition: transform 0.1s;
  }
</style>
