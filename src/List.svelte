<script>
	export let items;
</script>

{#each items as item}
	<svelte:component this={item.component} value={item.value} size={item.size}/>
{/each}