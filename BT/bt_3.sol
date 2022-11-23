// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8;

import "hardhat/console.sol";

contract Student{
    struct Student{
        uint256 roll_no;
        string name;
        string department;
    }

    Student[] students;

    function addStudent(uint256 roll_no, string memory name, string memory dept) public {
        Student memory stud = Student(roll_no, name, dept);
        students.push(stud);
    }

    function getStudent(uint256 roll_no) public view returns (string memory, string memory){
        for (uint256 i = 0; i< students.length; i+=1){
            Student memory stud = students[i];
            if (stud.roll_no==roll_no){
                return (stud.name, stud.department);
            }
        }
        return ("Not Found", "Not Found");
    }

    fallback() external {
        console.log("Err");
    }
}
