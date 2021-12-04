#!/usr/bin/env perl
use strict;
use warnings;
use Data::Dumper;

#I've reverted to teh dark side

open (my $fh, '<', '4.in');
chomp(my @sequence = split(',',<$fh>));


my @boards;
my @current_board;
while(my $line = <$fh>){ 
    chomp($line);
    next unless $line =~ m/\d+/;
    my @row = split(' ', $line);
    push @current_board,\@row;
    if (scalar @current_board  == 5) { 
        for my $i (0..5){ 
            push @current_board, [0,0,0,0,0,0]; 
        }
        my @copy = @current_board;
        push @boards,\@copy;
        undef @current_board;
    } 
} 

#print Dumper(@boards);

foreach my $num (@sequence){ 
    my @copy_board;

    foreach my $board (@boards){ 
        if (check_board($board,$num)){ 
            if (scalar @boards == 100) { 
                print "Found part 1 winner!\n";
                print score_board($board,$num); 
                print "\n";
            } 
            if (scalar @boards == 1) { 
                print "Found part 2 winner!\n";
                print score_board($boards[0],$num); 
                print "\n";
                exit;
            } 
        } else { 
            push (@copy_board, $board);
        } 
    } 
    @boards = @copy_board;
} 

sub score_board { 
    my $boardhash = shift;
    my @board = @$boardhash;
    my $number = shift;
    my $sum = 0; 
    for my $i (0..4){ 
        for my $j (0..4){ 
            if ($board[$i + 5 ][$j] == 0){ 
                $sum += $board[$i][$j];
            }
        }
    }
    #  print "$sum,$number\n";
    return $sum * $number;

} 
sub check_board { 
    my $boardhash = shift;
    my @board = @$boardhash;
    my $number = shift;
    for my $i (0..4){ 
        for my $j (0..4){ 
            if ($board[$i][$j] == $number){ 
                $board[$i + 5 ][$j] = 1;
                #column
                $board[10][$j]++;
                #row
                $board[$i + 5 ][5]++
            }
        } 
    } 
    #Check rows
    my $sum = 0;
    for my $i (5..9){ 
        if ($board[$i][5] == 5) { 
            #       print "found row from $number\n";
            return 1;
        }
    }
    #check columns
    for my $i (0..4) { 
        #print "checking ($board[10][$i]) \n";
        if ($board[10][$i] == 5) { 
            #print "found colunn from $number\n";
            return 1;
        } 
    }
    #check diaganol
    #  return 1 if $board[5][0] + $board[6][1] + $board[7][2] + $board[8][3] + $board[9][4] == 5;
    #return 1 if $board[5][4] + $board[6][3] + $board[7][2] + $board[8][1] + $board[9][0] == 5;
    return 0
} 
