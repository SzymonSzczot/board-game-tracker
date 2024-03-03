<script>
    import PlayerCurrentState from "./PlayerCurrentState.svelte";
    export let players;
</script>

<div>
    {#each players as player}
        <PlayerCurrentState {player}/>
    {/each}
</div>
