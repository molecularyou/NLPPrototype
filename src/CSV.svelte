<script>
  export let items = [];
</script>

<button
  disabled={items.length === 0}
  on:click={() => {
    let headers = [["PMID"].concat(Object.keys(items[0].selected))];
    let rows = items.map((item) => {
      return [[String(item.doi)].concat(
        Object.entries(item.selected).map(([key, selected]) => {
          if (selected.length > 0) {
            if (key !== 'umls'){
              return (
              '"' +
              selected
                .map((pos) =>
                  item.response.input.slice(pos.start, pos.end).join(" ")
                )
                .join("\n") +
              '"'
            );
            } else {
              return (
              '"' +
              selected.join("\n") +
              '"'
              );
            }
          } else {
            return '';
          }
        })
      )];
    });
    let csvContent =
      "data:text/csv;charset=utf-8," +
      headers
        .concat(rows)
        .map((e) => e.join(","))
        .join("\n");
    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "my_data.csv");
    document.body.appendChild(link); // Required for FF

    link.click();
  }}
>
  Export
</button>
