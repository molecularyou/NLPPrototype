<script>
  export let value;
  export let selected;
  let modifiedValue = [...value.input];

  $: text = modifiedValue.join(" ");
  const sample_sizes = value.size.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const fluids = value.fluids.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const sexes = value.sexes.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const ages = value.ages.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const omics = value.omics.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const controlGroups = value.controlGroups.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const healthyControlGroups = value.healthyControlGroups.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const analytes = value.analytes.map((pos) => ({
    text: value.input.slice(pos.start, pos.end).join(" "),
    start: pos.start,
    end: pos.end,
  }));
  const umlsMatches = value.umls.map((pos) => ({
    text: pos.text,
    start: pos.start,
    end: pos.end,
  }));
</script>

<div class="card">
  <p>{@html text}</p>
  <div class="grid-container">
    <div class="grid-item">
      <label for="samplesize">Sample Sizes:</label>
      <select
        name="samplesize"
        id="samplesize"
        multiple
        bind:value={selected.size}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.size.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
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
    <div class="grid-item">
      <label for="fluids">Possible Fluids:</label>
      <select
        name="fluids"
        id="fluids"
        multiple
        bind:value={selected.fluid}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.fluid.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each fluids as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="sexes">Possible Sexes:</label>
      <select
        name="sexes"
        id="sexes"
        multiple
        bind:value={selected.sex}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.sex.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each sexes as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="ages">Possible Ages:</label>
      <select
        name="ages"
        id="ages"
        multiple
        bind:value={selected.age}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.age.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each ages as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="omics">Possible Omics:</label>
      <select
        name="omics"
        id="omics"
        multiple
        bind:value={selected.omic}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.omic.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each omics as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="controlGroups">Possible Control Groups:</label>
      <select
        name="controlGroups"
        id="controlGroups"
        multiple
        bind:value={selected.controlGroup}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.controlGroup.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each controlGroups as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="healthyControlGroups">Possible Healthy Control Groups:</label>
      <select
        name="healthyControlGroups"
        id="healthyControlGroups"
        multiple
        bind:value={selected.healthyControlGroup}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.healthyControlGroup.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each healthyControlGroups as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="analytes">Possible Analytes:</label>
      <select
        name="analytes"
        id="analytes"
        multiple
        bind:value={selected.analyte}
        on:change={() => {
          modifiedValue = [...value.input];
          selected.analyte.forEach((item) => {
            modifiedValue[item.start] =
              '<div style="color:red;"><strong>' + modifiedValue[item.start];
            modifiedValue[item.end - 1] =
              modifiedValue[item.end - 1] + "</strong></div>";
          });
        }}
      >
        {#each analytes as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
    <div class="grid-item">
      <label for="umlsMatches">Possible UMLS:</label>
      <select
        name="umlsMatches"
        id="umlsMatches"
        multiple
        bind:value={selected.umls}
      >
        {#each umlsMatches as sample, index (sample.start)}
          <option id={index} value={{ start: sample.start, end: sample.end }}>
            {sample.text}
          </option>
        {:else}
          Nothing
        {/each}
      </select>
    </div>
  </div>
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
  .grid-container {
    display: flex;
    flex-wrap: wrap;
    gap: 50px;
  }
  .grid-item {
    text-align: center;
    flex: 1 1 150px;
  }
</style>
