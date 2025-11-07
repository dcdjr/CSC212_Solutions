// sudoku_checker

// Includes necessary libraries
#include <iostream>
#include <string>
#include <vector>

// Creates alias for 2D vector for less typing
using vec2D = std::vector<std::vector<int>>;

// Prototypes for functions
vec2D readAndStorePuzzle();
bool checkCols(vec2D storedPuzzle);
bool checkRows(vec2D storedPuzzle);
bool checkBoxes(vec2D storedPuzzle);
bool checkIfIntInVector(std::vector<int> vec, int element);

// Main function
int main() {
    vec2D storedPuzzle = readAndStorePuzzle();
    bool validSolution = checkCols(storedPuzzle) && checkRows(storedPuzzle) && checkBoxes(storedPuzzle);
    
    if (validSolution) {
        std::cout << "Solution is good!" << std::endl;
    }
    else {
        std::cout << "Wrong solution!" << std::endl;
    }
}

// Reads and stores a Sudoku puzzle as a 9x9 2D vector
vec2D readAndStorePuzzle() {
    vec2D puzzle(9, std::vector<int>(9));

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            std::cin >> puzzle[i][j];
        }
    }

    return puzzle;
}

// Checks the columns to ensure they don't have duplicate digits
bool checkCols(vec2D storedPuzzle) {
    std::vector<int> seen = {};
    for (int i = 0; i < 9; i++) {
        seen.clear();
        for (int j = 0; j < 9; j++) {
            if (checkIfIntInVector(seen, storedPuzzle[j][i])) {
                return false;
            } else {
                seen.push_back(storedPuzzle[j][i]);
            }
        }
    }

    return true;
}

// Checks the rows to ensure they don't have duplicate digits
bool checkRows(vec2D storedPuzzle) {
    std::vector<int> seen = {};
    for (int i = 0; i < 9; i++) {
        seen.clear();
        for (int j = 0; j < 9; j++) {
            if (checkIfIntInVector(seen, storedPuzzle[i][j])) {
                return false;
            } else {
                seen.push_back(storedPuzzle[i][j]);
            }
        }
    }

    return true;
}

// Checks the 9 boxes to ensure they don't have duplicate digits
bool checkBoxes(vec2D storedPuzzle) {
    for (int i = 1; i < storedPuzzle.size(); i += 3) {
        for (int j = 1; j < storedPuzzle.size(); j += 3) {
            std::vector<int> seen = {};
            for (int h = i - 1; h <= i + 1; h++) {
                for (int k = j - 1; k <= j + 1; k++) {
                    if (checkIfIntInVector(seen, storedPuzzle[h][k])) {
                        return false;
                    } else {
                        seen.push_back(storedPuzzle[h][k]);
                    }
                }
            }
        }
    }
    return true;
}

// Checks if element is in a vector
bool checkIfIntInVector(std::vector<int> vec, int element) {
    for (int i = 0; i < vec.size(); i++) {
        if (element == vec[i]) {
            return true;
        }
    }

    return false;
}