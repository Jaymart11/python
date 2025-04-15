/** @format */

const items = [
  {id: 2, seqId: 4, parent: 5, name: 'index.tsx'},
  {id: 3, seqId: 3, parent: 1, name: 'Sidebar'},
  {id: 4, seqId: 5, parent: 1, name: 'Table'},
  {id: 7, seqId: 5, parent: 5, name: 'SelectableDropdown.tsx'},
  {id: 5, seqId: 2, parent: 1, name: 'AssignmentTable'},
  {id: 1, seqId: 1, parent: null, name: 'components'},
  {id: 6, seqId: 2, parent: null, name: 'controllers'},
];

const finalItems = transformItems(items);

function transformItems(items) {
  items.forEach(item => {
    const {seqId, parent, id, name} = item;
    if (parent === null) {
      item.depth = 0;
    }
  });

  items.forEach(item => {
    const {seqId, parent, id, name} = item;
    if (parent !== null) {
      console.log(depthValue(id));
    }
  });

  function depthValue(id) {
    let valueItem;
    items.forEach(item => {
      if (item.parent === id) {
        valueItem = item;
      }
    });
    return valueItem;
  }

  console.log(items);
}
