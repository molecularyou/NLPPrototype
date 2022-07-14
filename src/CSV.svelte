<script>
  export let items = [];
</script>

<button
  disabled={items.length === 0}
  on:click={() => {
    let headers = [["doi"].concat(Object.keys(items[0].selected))];
    let rows = items.map((item) => {
      return [[String(item.doi)].concat(
        Object.values(item.selected).map((selected) => {
          if (selected.length > 0) {
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
            return '';
          }
        })
      )];
    });
    console.log(headers);
    console.log(rows.map((e) => console.log(e)));
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
