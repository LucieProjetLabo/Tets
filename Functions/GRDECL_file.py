def write_2_values( file, value ):
    file.write( '%f\n%f\n'%(value, value ) )

def write_zcorn_line( zgrid, xygrid, file, iv, iw, write_n_values ):
    file.write( '%f\n'% zgrid[iw][0][iv] )
    for iu in range( 1, xygrid.nu_-1 ): # Consider only the non-boundary pillars
        write_n_values( file, zgrid[iw][iu][iv] )
    file.write( '%f\n'%zgrid[iw][xygrid.nu_-1][iv] )
    
def write_zcorn_plane(zgrid, xygrid, file, iw ):
    # Write the first line
    write_zcorn_line( zgrid, xygrid, file, 0, iw, write_2_values )
    for iv in range ( 1,  xygrid.nv_ - 1 ):
        write_zcorn_line( zgrid, xygrid, file, iv, iw, write_2_values )
        write_zcorn_line( zgrid, xygrid, file, iv, iw, write_2_values )
        # Write the last line
    write_zcorn_line( zgrid, xygrid, file, xygrid.nv_ - 1, iw, write_2_values )

def write_eclipse_pillars( zgrid, xygrid, file ):    
    top = 0
    bottom = len(zgrid)-1
    
    # Write the pillars
    file.write("\nCOORD\n")
    for iv in range( xygrid.nv_ ):
        for iu in range(  xygrid.nu_ ):
            pillarcoords = xygrid.point(iu, iv)
            file.write( '%f\t'%pillarcoords[0] )
            file.write( '%f\t'%pillarcoords[1] )
            file.write( '%f\t'%zgrid[top][iu][iv] )
            file.write( '%f\t'%pillarcoords[0] )
            file.write( '%f\t'%pillarcoords[1] )
            file.write( '%f\n'%zgrid[bottom][iu][iv] )

# Write the eclipse file. GRDECL
def write_eclipse( zgrid, xygrid, filename ):    
    file = open( filename, "w+") 
    top = 0
    bottom = len(zgrid)-1
    # Write the grid geometry
    file.write("SPECGRID\n")
    file.write('%d %d %d 1 F /\n'%(xygrid.nu_-1, xygrid.nv_-1, bottom ) )
    
    # Write the pillars
    write_eclipse_pillars( zgrid, xygrid, file )
    
    # Write the corners of pillars
    file.write( '/\n\nZCORN\n' )
    write_zcorn_plane( zgrid, xygrid, file, 0 )
    for iw in range ( 1, len(zgrid)-1 ):
        write_zcorn_plane( zgrid, xygrid, file, iw )
        write_zcorn_plane( zgrid, xygrid, file, iw )
    write_zcorn_plane( zgrid, xygrid, file, len(zgrid)-1 )
        
    file.write( '/\n' )