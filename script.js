let s = prompt("Enter a list of values separated by commas:");
let a = s.split(",");
a = a.map(value => parseFloat(value.trim()));

function findMaxElement(a) {
    if (a.length === 0) {
        return "Array is empty";
    }
    let max = a[0];
    for (let i = 1; i < a.length; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }

    return max;
}

let max = findMaxElement(a);
console.log("Maximum element:", max);
