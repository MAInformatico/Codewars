using namespace std;

string reverse_letter(const string &str){
    string result;
    string alphabet="abcdefghijklmnopqrstuvwxyz";
    for(int i=str.size()-1;i>=0;i--){
      for(int j=0;j<alphabet.size();j++){
        if(str[i]==alphabet[j]) result.push_back(str[i]);
      }
    }
    return result;
}
