// console.log("script file")
// List with handle
Sortable.create(list_1_1, {
    group: 'test1',
    handle: '.fa-arrows-alt',
    animation: 150
});
// List with handle
Sortable.create(list_1_2_1, {
    group: 'test1',
    handle: '.fa-arrows-alt',
    animation: 150
});
function uuidv4() {
    return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
}
$(function () {
    setToggles()

    $('#add-group-button').on('click', function () {
        var newName = $('#group-name-input').val()
        console.log(newName)
        addGroupName('group_parent', newName, uuidv4())
    })

});
function setToggles() {
    $('.list-group-item-toggle').on('click', function () {
        $('.fa', this)
            .toggleClass('fa-caret-right')
            .toggleClass('fa-caret-down');
    });
}
// List with handle
Sortable.create(group_1, {
    group: 'test2',
    handle: '.fa-arrows-alt',
    animation: 150
});
// List with handle
Sortable.create(group_2, {
    group: 'test2',
    handle: '.fa-arrows-alt',
    animation: 150
});
// List with handle
Sortable.create(investigations_2, {
    group: 'test2',
    handle: '.fa-arrows-alt',
    animation: 150
});
Sortable.create(group_parent, {
    group: 'test3',

    animation: 150
});
function addGroupName(groupContainerId, groupName, groupID) {
    //console.log(groupContainerId, groupName, groupID)
    var groupContainer = $("#" + groupContainerId)
    var values = { groupName: groupName, groupID: groupID }
    var template_string =
        `<div class="list-group-item list-group-item-toggle"><a href="#${values.groupID}"
    class="list-group-item list-group-item-action" data-toggle="collapse">
    <span class="fa fa-caret-right"></span>${groupName}</a>
        <div id="${groupID}" class="list-group collapse show">

        </div>
    </div>`;
    //console.log(values)
    //console.log(template_string)
    groupContainer.append($(template_string))
    Sortable.create($("#" + groupID)[0], {
        group: 'test2',
        handle: '.fa-arrows-alt',
        animation: 150
    });
    setToggles()
};
