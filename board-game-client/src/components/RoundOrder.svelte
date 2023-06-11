
<style>
    .player {
        border-style: dashed;
        margin: 6px;
    }

    .isCurrent {
        border-style: solid
    }


</style>

<script>
    export let players;
    export let currentRoundTime
    $: roundTime = currentRoundTime

</script>

<div>
    {#each players as {name, isCurrent}}
        <div class="player" class:isCurrent>
            {name}
        {#if isCurrent}
            <span>{roundTime}</span>
        {/if}
        </div>
    {/each}
</div>
