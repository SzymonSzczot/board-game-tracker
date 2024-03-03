
<script>
    import PointCard from "./PointCard.svelte";
    export let points;

</script>

<div style="display: flex; flex-wrap: wrap; justify-content: center">
    {#each points as point}
        <PointCard {...point}/>
    {:else}
        <PointCard value="..." icon="https://thenounproject.com/api/private/icons/2395229/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=752&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0"/>
    {/each}
</div>
