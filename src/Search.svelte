<script>
  export let onChangeDOI;
  export let onChangeIDType;
  export let onChangeSubmitType;
  export let onClick;
  export let disableSubmit;
  export let iDType;
  export let submitType;
</script>

<div id="flex-container">
  <select name="idtype" id="idtype" bind:value={iDType} on:change={(e) => onChangeIDType(e.target.value)}>
    <option value="doi">DOI</option>
    <option value="pmid">PMID</option>
  </select>
  <input
    type="search"
    id="id"
    name="id"
    on:change={(e) => onChangeDOI(e.target.value)}
    placeholder="ID"
  />
  <select name="type" id="type" bind:value={submitType} on:change={(e) => onChangeSubmitType(e.target.value)}>
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
