#include <iostream>
#include <windows.h>
#include <conio.h>
using namespace std;
HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

struct map_block
{
     char symbol;
     int color;
};

struct player
{
     map_block appearance;
     int x;
     int y;
};

map_block *make_map(int size_x, int size_y)
{
     map_block* mapa = (map_block*)malloc(size_x*size_y*sizeof(map_block));
     return mapa;
}

void fill_map(map_block* mapa, int color, int size_x, int size_y)
{
     for(int i=0; i<size_x*size_y; i++){
          mapa[i].symbol = 'o';
          mapa[i].color = color;
     }
}

void draw_frame(map_block* framebuff, int size_x, int size_y)
{
     COORD c;
     for(int y=0; y<size_y; y++){
          for(int x=0; x<size_x; x++){
               c.Y = y;
               c.X = x;
               SetConsoleTextAttribute(hConsole, framebuff[size_y*y+x].color);
               SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
               printf("%c", framebuff[size_y*y+x].symbol);
          }
     }
}

player makePlayer(char symbol, int color, int position_x, int position_y)
{
     player p;
     p.appearance.color = color;
     p.appearance.symbol = symbol;
     p.x = position_x;
     p.y = position_y;
     return p;
}

void set_player(player p, map_block* framebuff, int map_size_y)
{
     framebuff[p.y*map_size_y+p.x].color = p.appearance.color;
     framebuff[p.y*map_size_y+p.x].symbol = p.appearance.symbol;
}

void set_map(map_block* mapa, map_block* framebuff, int map_size_x, int map_size_y)
{
     for(int y=0; y<map_size_y; y++){
          for(int x=0; x<map_size_x; x++){
               framebuff[y*map_size_y+x] = mapa[y*map_size_y+x];
          }
     }
}

int main()
{
     map_block* mapa = make_map(20, 20);
     map_block* framebuff = make_map(20, 20);
     fill_map(mapa, 8, 20, 20);
     player p = makePlayer('A', 2, 0, 0);
     char move_player = '0';
     int points = 0;
     printf("Press any key to start!");
     while(1){
          move_player = getch();
          if(move_player == 'd' && p.x < 19){
               p.x++;
          }
          if(move_player == 'a' && p.x > 0){
               p.x--;
          }
          if(move_player == 'w' && p.y > 0){
               p.y--;
          }
          if(move_player == 's' && p.y < 19){
               p.y++;
          }
          set_map(mapa, framebuff, 20, 20);
          set_player(p, framebuff, 20);
          draw_frame(framebuff, 20, 20);
          printf("\nPoints: %d", points);
     }

     return 0;
}
