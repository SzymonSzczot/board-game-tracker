
<style>
    .playerHeader {
        padding: 10px;
    }
</style>

<script>
    export let player;
</script>


<div class="playerHeader">
    <p>{player.name}</p>
    <p>points: {player.points.reduce((accumulator, obj) => accumulator + obj.value, 0)}</p>
{#if player.isCurrent}
    <div class="btn btn-outline-success" type="button">Zakończ rundę ({player.roundTime}s)</div>
{/if}
</div>
