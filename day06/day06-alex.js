import React, {useState, useEffect} from "react";
import day06 from './day06-alex.txt';


const Day06 = () => {

    const [result, setResult] = useState([]);

    function test(a_string) {

        var found_1 = false
        var found_2 = false
        for (var i = 0; i < a_string.length; i++) {
            //console.log(i)
            var chunk = a_string.slice(i, i+4)
            var chunk_2 = a_string.slice(i, i+14)
            //console.log(chunk)
            // check for duplicates
            function hasRepeats (str) {
                return /(.).*\1/.test(str);
            }
            //console.log(hasRepeats(chunk))
            if (hasRepeats(chunk) === false & found_1 === false) {
                //console.log("unique:", chunk, "at position", i+4)
                var part_01 = i+4
                found_1 = true
            }
            if (hasRepeats(chunk_2) === false & found_2 === false) {
                //console.log("unique", chunk_2, "at position", i+14)
                var part_02 = i+14
                found_2 = true
            }
        }
        var results = [part_01, part_02]

        return (results)
    }
    
    fetch(day06)
    .then(r => r.text())
    .then(text => {
        setResult(test(text))
    });

    return(
        <div>
            Hi! The result of day06 part 1 is: {result[0]} <div> </div>
            And Part 2 is {result[1]}
        </div>)

}
export default Day06


