#include <string>
#include <unordered_map>

std::string duplicate_encoder(const std::string& word){
    std::unordered_map<char, int> charCount;
    for(char c : word) charCount[tolower(c)]++;
    std::string result = "";
    for(char c : word) result += (charCount[tolower(c)] > 1)? ')' : '(';
    return result;
}
