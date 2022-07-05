<script>
  export let value;
  export let size;
  const text = value.join(" ");
  const sample_sizes = size.map((pos) => ({
    text: value.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
</script>

<div class="card">
  <p>{text}</p>
  <select name="samplesize" id="samplesizelist">
    {#each sample_sizes as todo, index (todo.start)}
      <option id={index}>
        {todo.text}
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
