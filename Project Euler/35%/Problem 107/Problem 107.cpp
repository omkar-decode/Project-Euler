#include <bits/stdc++.h>

using namespace std;

typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef vector< pair<int, int> > vpi;

float distance(float x1, float y1, float x2, float y2) {
    float dist = sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)));
    
    return dist;
}

bool intersect(vpi s1, vpi s2) {
    int xmax1 = max(s1[0].first, s1[1].first, s1[2].first, s1[3].first);
    int xmax2 = max(s2[0].first, s2[1].first, s2[2].first, s2[3].first);
    
    int xmin1 = min(s1[0].first, s1[1].first, s1[2].first, s1[3].first);
    int xmin2 = min(s2[0].first, s2[1].first, s2[2].first, s2[3].first);
    
    int ymax1 = max(s1[0].second, s1[1].second, s1[2].second, s1[3].second);
    int ymax2 = max(s2[0].second, s2[1].second, s2[2].second, s2[3].second);
    
    int ymin1 = min(s1[0].second, s1[1].second, s1[2].second, s1[3].second);
    int ymin2 = min(s2[0].second, s2[1].second, s2[2].second, s2[3].second);    
    
    if(xmax1<=xmax2 && xmin1>=xmin2 && ymax1<=ymax2 && ymin1>=ymin2) {
        return true;
    }
    if(xmax1>=xmax2 && xmin1<=xmin2 && ymax1>=ymax2 && ymin1<=ymin2) {
        return true;
    }
    
    if(xmax1<xmin2 || xmax2<xmin1 || ymax1<ymin2 || ymax2<ymin1) {
        return false;
    }
    
    float mpx1 = ((float)xmin1 + (float)xmax1)/((float)2);
    float mpy1 = ((float)ymin1 + (float)ymax1)/((float)2);
    
    float mpx2 = ((float)xmin2 + (float)xmax2)/((float)2);
    float mpy2 = ((float)ymin2 + (float)ymax2)/((float)2);
        
    float side1 = ((float)xmax1 - (float)xmin1);
    float diag2 = ((float)xmax2 - (float)xmin2);
    
    float side2 = diag2 / sqrt(2);
    float diag1 = side1 * sqrt(2);
    
    float centreSep = distance(mpx1, mpy1, mpx2, mpy2);
    
    if(centreSep<=(side1 + diag2) && centreSep<=(side2 + diag1)) {
        return true;
    }
}


int main()
{
    vpi sq1;
    vpi sq2;
    
    int x, y;
    for(int i=0; i<4; i++) {
        cin >> x >> y;
        sq1.push_back({x, y});
    }
     
    for(int i=0; i<4; i++) {
        cin >> x >> y;
        sq2.push_back({x, y});
    }
    
    
}
