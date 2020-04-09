function staircase(n) {
    let str = ''
    // important to start from 1, otherwise adds a line with nothing
    for(let i = 1; i <= n; i++) {
        // use repeat to repeat a string a set number of times
        // use newline to move the cursor to next line, otherwise prints all one line
        str += (' '.repeat(n - i) + '#'.repeat(i) + '\n')
    }
    console.log(str)
}

staircase(6)