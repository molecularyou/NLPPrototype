<script>
  export let value;
  export let size;
  let modifiedValue = [...value];
  let selected = [];
  $: text = modifiedValue.join(" ");
  const sample_sizes = size.map((pos) => ({
    text: value.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
</script>

<div class="card">
  <p>{@html text}</p>
  <label for="samplesize">Sample Sizes:</label>
  <select
    name="samplesize"
    id="samplesize"
    multiple
    bind:value={selected}
    on:change={() => {
      modifiedValue = [...value];
      selected.forEach((item) => {
        modifiedValue[item.start] = '<div style="color:red;"><strong>' + modifiedValue[item.start];
        modifiedValue[item.end] = modifiedValue[item.end] + '</strong></div>';
      });
    }}
  >
    {#each sample_sizes as sample, index (sample.start)}
      <option id={index} value={{ start: sample.start, end: sample.end }}>
        {sample.text}
      </option>
    {:else}
      Nothing
    {/each}
  </select>
</div>

<style>
  .card {
    margin: 0.5em;
    padding: 0.5em 0.5em 0.5em 0.5em;
    border: 1px solid #eee;
    border-radius: 4px;
    box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    min-height: 5em;
  }
</style>
