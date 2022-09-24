function initSortables() {
    // List with handle
    Sortable.create($("#draggable-1")[0], {
        group: 'drag-group-1',
        handle: '.fa-arrows-alt',
        animation: 150
    });
    Sortable.create($("#group-1")[0], {
        group: 'drag-group-1',
        handle: '.fa-arrows-alt',
        animation: 150
    });
    Sortable.create($("#group-2")[0], {
        group: 'drag-group-1',
        handle: '.fa-arrows-alt',
        animation: 150
    });
    Sortable.create($("#group-parent")[0], {
        group: 'parent-group',
        animation: 150
    });
    Sortable.create($("#group-parent-2")[0], {
        group: 'parent-group',
        animation: 150
    });
}
function setToggles() {
    $('.list-group-item-toggle').on('click', function () {
        $('.fa', this)
            .toggleClass('fa-caret-right')
            .toggleClass('fa-caret-down');
    });
}
function setToggles2(elements) {
    elements.on('click', function () {
        $('.fa', this)
            .toggleClass('fa-caret-right')
            .toggleClass('fa-caret-down');
    });
}
function initAddGroupButton() {
    $('#add-group-button').on('click', function () {
        var newName = $('#group-name-input').val()
        console.log(newName)
        addGroupName('group-parent-2', newName, uuidv4())
    })
}
function addGroupName(groupContainerId, groupName, groupID) {
    //console.log(groupContainerId, groupName, groupID)
    var groupContainer = $("#" + groupContainerId)
    // var values = { groupName: groupName, groupID: groupID }
    var template_string =
        `<div class="list-group-item list-group-item-toggle"><a href="#${groupID}"
    class="list-group-item list-group-item-action" data-toggle="collapse">
    <span class="fa fa-caret-down"></span>${groupName}</a>
        <div id="${groupID}" class="list-group collapse show">

        </div>
    </div>`;
    //console.log(values)
    //console.log(template_string)
    groupContainer.append($(template_string))
    Sortable.create($("#" + groupID)[0], {
        group: 'drag-group-1',
        handle: '.fa-arrows-alt',
        animation: 150
    });
    setToggles()
};
function uuidv4() {
    return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
}
$(function () {
    setToggles()
    // setToggles2($('.list-group-item-toggle'))
    initAddGroupButton()
    initSortables()



});
