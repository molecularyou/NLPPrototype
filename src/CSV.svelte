<script>
  export let items = [];
</script>

<button
  disabled={items.length === 0}
  on:click={() => {
    let headers = [Object.keys(items[0].selected)];
    let rows = items.map((item) => {
      return Object.values(item.selected).map((selected) => {
        if (selected.length > 0) {
          return '"' + selected.map((pos) =>
            item.response.input.slice(pos.start, pos.end).join(" ")
          ).join("\n") + '"';
        } else {
          return [];
        }
      });
    });
    console.log(rows);
    let csvContent =
      "data:text/csv;charset=utf-8," + headers.concat(rows).map((e) => e.join(",")).join("\n");
    var encodedUri = encodeURI(csvContent);
    window.open(encodedUri);
  }}
>
  Export
</button>
